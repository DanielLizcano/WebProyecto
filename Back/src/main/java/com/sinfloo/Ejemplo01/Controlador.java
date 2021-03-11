package com.sinfloo.Ejemplo01;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@CrossOrigin(origins = "http://localhost:4200", maxAge = 3600)
@RestController
@RequestMapping({"/personas"})
public class Controlador {
    @Autowired
    PersonaService service;
    public List<Persona>listar(){
        return service.listar();
    }
    @PostMapping
    public Persona agregar(@RequestBody Persona p){
        return service.add(p);
    }
    @GetMapping(path = {"/{id}"})
    public Persona listarId(@PathVariable ("id")int id){
        return service.listarId(id);
    }
    @PutMapping(path = {"/{id}"})
    public Persona editar(@RequestBody Persona p, @PathVariable("id") int id){
    p.setId(id);
    return service.edit(p);
    }
    @DeleteMapping(path = {"/{id}"})
    public Persona delete(@PathVariable("id") int id){
        return service.delete(id);

    }
}
