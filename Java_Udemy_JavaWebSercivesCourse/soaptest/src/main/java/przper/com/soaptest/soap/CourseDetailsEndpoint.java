package przper.com.soaptest.soap;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.ws.server.endpoint.annotation.Endpoint;
import org.springframework.ws.server.endpoint.annotation.PayloadRoot;
import org.springframework.ws.server.endpoint.annotation.RequestPayload;
import org.springframework.ws.server.endpoint.annotation.ResponsePayload;

import com.przper.courses.CourseDetails;
import com.przper.courses.DeleteCourseDetailsRequest;
import com.przper.courses.DeleteCourseDetailsResponse;
import com.przper.courses.GetAllCourseDetailsRequest;
import com.przper.courses.GetAllCourseDetailsResponse;
import com.przper.courses.GetCourseDetailsRequest;
import com.przper.courses.GetCourseDetailsResponse;

import przper.com.soaptest.soap.bean.Course;
import przper.com.soaptest.soap.exception.CourseNotFoundException;
import przper.com.soaptest.soap.service.CourseDetailsService;
import przper.com.soaptest.soap.service.CourseDetailsService.Status;

@Endpoint
public class CourseDetailsEndpoint {

	@Autowired
	CourseDetailsService service;

	// method
	// input = GetCourseDetailsRequest
	// output = GetCourseDetailsResponse

	// http://przper.com/courses
	// GetCourseDetailsRequest

	@PayloadRoot(namespace = "http://przper.com/courses", localPart = "GetCourseDetailsRequest")
	@ResponsePayload
	public GetCourseDetailsResponse processCourseDetailsRequest(@RequestPayload GetCourseDetailsRequest request) {
		Course course = service.findById(request.getId());

		if (course == null)
			throw new CourseNotFoundException("Invalid Course Id: " + request.getId());

		return mapCourseDetails(course);
	}

	@PayloadRoot(namespace = "http://przper.com/courses", localPart = "GetAllCourseDetailsRequest")
	@ResponsePayload
	public GetAllCourseDetailsResponse processAllCourseDetailsRequest(
			@RequestPayload GetAllCourseDetailsRequest request) {
		List<Course> courses = service.findAll();

		return mapAllCourseDetails(courses);
	}

	@PayloadRoot(namespace = "http://przper.com/courses", localPart = "DeleteCourseDetailsRequest")
	@ResponsePayload
	public DeleteCourseDetailsResponse deleteCourseDetailsRequest(@RequestPayload DeleteCourseDetailsRequest request) {
		Status status = service.deleteById(request.getId());

		DeleteCourseDetailsResponse response = new DeleteCourseDetailsResponse();
		response.setStatus(mapStatus(status));

		return response;
	}

	private com.przper.courses.Status mapStatus(Status status) {
		if (status == Status.FAILURE)
			return com.przper.courses.Status.FAILURE;
		return com.przper.courses.Status.SUCCESS;
	}

	private GetCourseDetailsResponse mapCourseDetails(Course course) {
		GetCourseDetailsResponse response = new GetCourseDetailsResponse();
		response.setCourseDetails(mapCourse(course));
		return response;
	}

	private GetAllCourseDetailsResponse mapAllCourseDetails(List<Course> courses) {
		GetAllCourseDetailsResponse response = new GetAllCourseDetailsResponse();
		for (Course course : courses) {
			CourseDetails mapCourse = mapCourse(course);
			response.getCourseDetails().add(mapCourse);
		}
		return response;
	}

	private CourseDetails mapCourse(Course course) {
		CourseDetails courseDetails = new CourseDetails();
		courseDetails.setId(course.getId());
		courseDetails.setName(course.getName());
		courseDetails.setDescription(course.getDescription());
		return courseDetails;
	}
}
