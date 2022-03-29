package com.laozi.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.Map;

@Controller
public class myTestController {

    @GetMapping("/test")
    public String test(Model model, @RequestParam Map<String,Object> Pmap){
        String name = (String) Pmap.get("name");
        String passward = (String) Pmap.get("passward");
        System.out.println(name);
        System.out.println(passward);
        model.addAttribute("msg","hello");
        return "test";
    }

    @PostMapping("/test1")
    @ResponseBody
    public String test1(@RequestParam Map<String,Object> Pmap){
        return "author";
    }
}
