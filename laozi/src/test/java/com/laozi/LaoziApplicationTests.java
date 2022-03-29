package com.laozi;

import com.laozi.service.AuthorService;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class LaoziApplicationTests {

    @Autowired
    private AuthorService authorService;

    @Test
    void contextLoads() {
        System.out.println(authorService.getAuthorList());
        System.out.println(1);
    }

}
