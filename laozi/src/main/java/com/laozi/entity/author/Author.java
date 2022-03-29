package com.laozi.entity.author;

import lombok.Data;
import org.springframework.stereotype.Component;

@Data
public class Author {
    private String id;
    private String author_name;
    private String author_dynasty;
    private String author_intro;
    private String author_pic;

}

