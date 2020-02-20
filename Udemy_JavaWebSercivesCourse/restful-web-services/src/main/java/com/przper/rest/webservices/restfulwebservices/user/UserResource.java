package com.przper.rest.webservices.restfulwebservices.user;

import java.net.URI;
import java.util.List;

import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
//import org.springframework.hateoas.EntityModel;
//import org.springframework.hateoas.server.mvc.WebMvcLinkBuilder;

//import static org.springframework.hateoas.server.mvc.WebMvcLinkBuilder.*;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.support.ServletUriComponentsBuilder;

@RestController
public class UserResource {

	@Autowired
	private UserDaoService service;

	// GET /users
	// retrieveAllUsers
	@GetMapping("/users")
	public List<User> retrieveAllUsers() {
		return service.findAll();
	}

	/*
	 * // GET /users/{id} // retrieveUser(int id)
	 * 
	 * @GetMapping("/users/{id}") public EntityModel<User>
	 * retrieveUser(@PathVariable int id) { User user = service.findOne(id); if
	 * (user == null) { throw new UserNotFoundException("id-" + id); } //
	 * "all-users", SERVER_PATH + "/users" // retrieveAllUsers EntityModel<User>
	 * model = new EntityModel<>(user); WebMvcLinkBuilder linkTo =
	 * linkTo(methodOn(this.getClass()).retrieveAllUsers());
	 * model.add(linkTo.withRel("all-users")); //hateoas return model; }
	 */

	//without hateoas
	@GetMapping("/users/{id}")
	public User retrieveUser(@PathVariable int id) {
		User user = service.findOne(id);

		if (user == null)
			throw new UserNotFoundException("id-" + id);

		return user;
	}

	// CREATED
	// input - details of user
	// output - CREATED & return created URI
	@PostMapping("/users")
	public ResponseEntity<Object> createUser(@Valid @RequestBody User user) {
		User savedUser = service.save(user);
		// CREATED
		// /users/{id} savedUser.getId
		URI location = ServletUriComponentsBuilder.fromCurrentRequest().path("/{id}").buildAndExpand(savedUser.getId())
				.toUri();

		return ResponseEntity.created(location).build();
	}

	@DeleteMapping("/users/{id}")
	public void deleteUser(@PathVariable int id) {
		User user = service.deleteById(id);
		if (user == null) {
			throw new UserNotFoundException("id-" + id);
		}
	}

	/*
	 * // GET /users/{id}/posts // retrieveAllPosts(int id)
	 * 
	 * @GetMapping("/users/{id}/posts") public User retrieveAllPosts(@PathVariable
	 * int id) { User user = service.findOne(id); if (user == null) { throw new
	 * UserNotFoundException("id-"+id); } List<Post> posts =
	 * postService.findAll(id); return posts; }
	 * 
	 * // CREATED // input - details of post, user id // output - CREATED & return
	 * created URI
	 * 
	 * @PostMapping("/users/{id}/posts") public ResponseEntity<Object>
	 * createPost(@PathVariable int id, @RequestBody Post post) { User user =
	 * service.findOne(id); //CREATED // /users/{id} savedUser.getId Post post =
	 * postService.save(user.getId(), post)
	 * 
	 * URI location = ServletUriComponentsBuilder .fromCurrentRequest()
	 * .path("/{id}") .buildAndExpand(savedUser.getId()). .path("/posts/{post_id}")
	 * .buildAndExpand(post.getId()). .toUri();
	 * 
	 * return ResponseEntity.created(location).build(); }
	 * 
	 * // GET /users/{id}/posts/{post_id} // retrievePost(int id, int post_id)
	 * 
	 * @GetMapping("/users/{id}/posts/{post_id}") public User
	 * retrievePost(@PathVariable int id, @PathVariable int post_id) { User user =
	 * service.findOne(id); if (user == null) { throw new
	 * UserNotFoundException("id-"+id); } Post post = postService.findOne(id,
	 * post_id); return post; }
	 * 
	 */
}
