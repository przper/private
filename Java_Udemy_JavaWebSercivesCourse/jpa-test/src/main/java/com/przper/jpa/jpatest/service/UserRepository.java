package com.przper.jpa.jpatest.service;

import org.springframework.data.jpa.repository.JpaRepository;

import com.przper.jpa.jpatest.entity.User;

public interface UserRepository extends JpaRepository<User, Long> {

}
