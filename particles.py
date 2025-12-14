"""
Docstring for particles
"""
from random import random, choice
from __future__ import annotations

class Particle:
    #NOTE might add colors with colorama or termcolor in the future, excluding the need for unique chars
    def __init__(self, char: str, particles: list[Particle]): # in regular PL simulators you would use colors, since this is ASCII, we use char
        self.char = char
        # particles is a list of all particle objects
        self.particles = particles
    

    def update_particle_list(self, particles: list[Particle]) -> None:
        """
        Docstring for update_particle_list
        
        :param self: Description
        :param particles: Description
        :type particles: list[particle]

        updates the list of particles based on the state of
        the global particles list, which might change.
        """
        self.particles = particles
    

    def create_matrix_rel_to_self(self, vector_force_range: float | int, ) -> tuple[tuple[int, float], ...]: # tuple[int, float] for however long self.particles is
        """
        Docstring for create_matrix_rel_to_self
        
        :param self: Description
        :return: Description
        :rtype: tuple[tuple[int, float]]

        the reutrned tuple contains:
        - tuples for each index into self.particles
        inside each tuple contains:
        - the index of the interacting particle in self.particles
        - a force which will be applied
        """

        final_matrix = [
        (i, choice([1, -1]) * random() * vector_force_range)
        for i in range(len(self.particles))
        ]
        return final_matrix

    def get_current_velocity(
        cur_position: tuple[int, int],
        list_of_particle_info: list[list[list[int, int], float | int, float | int]],
        area_of_effect: int, # the radius of an invisible circle of effect around particles

    )


            
















