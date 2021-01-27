import atheris
import pytest
import sys

from .utils import reach_api

def test_ability():
    def get_ability(name):
        reach_api("ability", {"name": str(name)})

    atheris.Setup([sys.argv[0], '-runs=100'], get_ability)
    atheris.Fuzz()

def test_berry():
    def get_berry(name):
        reach_api("berry", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_berry)
    atheris.Fuzz()


def test_berry_firmness():
    def get_berry_firmness(name):
        reach_api("berry-firmness", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_berry_firmness)
    atheris.Fuzz()


def test_berry_flavor():
    def get_berry_flavor(name):
        reach_api("berry-flavor", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_berry_flavor)
    atheris.Fuzz()


def test_characteristic():
    def get_characteristic(name):
        reach_api("characteristic", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_characteristic)
    atheris.Fuzz()


def test_contest_type():
    def get_contest_type(name):
        reach_api("contest-type", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_contest_type)
    atheris.Fuzz()


def test_contest_effect():
    def get_contest_effect(name):
        reach_api("contest-effect", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_contest_effect)
    atheris.Fuzz()


def test_egg_group():
    def get_egg_group(name):
        reach_api("egg-group", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_egg_group)
    atheris.Fuzz()


def test_encounter_method():
    def get_encounter_method(name):
        reach_api("encounter-method", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_encounter_method)
    atheris.Fuzz()


def test_encounter_condition():
    def get_encounter_condition(name):
        reach_api("encounter-condition", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_encounter_condition)
    atheris.Fuzz()


def test_encounter_condition_value():
    def get_encounter_condition_value(name):
        reach_api("encounter-condition-value", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_encounter_condition_value)
    atheris.Fuzz()


def test_evolution_chain():
    def get_evolution_chain(name):
        reach_api("evolution-chain", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_evolution_chain)
    atheris.Fuzz()


def test_evolution_trigger():
    def get_evolution_trigger(name):
        reach_api("evolution-trigger", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_evolution_trigger)
    atheris.Fuzz()


def test_generation():
    def get_generation(name):
        reach_api("generation", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_generation)
    atheris.Fuzz()


def test_gender():
    def get_gender(name):
        reach_api("gender", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_gender)
    atheris.Fuzz()


def test_growth_rate():
    def get_growth_rate(name):
        reach_api("growth-rate", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_growth_rate)
    atheris.Fuzz()


def test_item():
    def get_item(name):
        reach_api("item", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_item)
    atheris.Fuzz()


def test_item_category():
    def get_item_category(name):
        reach_api("item-category", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_item_category)
    atheris.Fuzz()


def test_item_attribute():
    def get_item_attribute(name):
        reach_api("item-attribute", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_item_attribute)
    atheris.Fuzz()


def test_item_fling_effect():
    def get_item_fling_effect(name):
        reach_api("item-fling-effect", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_item_fling_effect)
    atheris.Fuzz()


def test_item_pocket():
    def get_item_pocket(name):
        reach_api("item-pocket", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_item_pocket)
    atheris.Fuzz()


def test_language():
    def get_language(name):
        reach_api("language", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_language)
    atheris.Fuzz()


def test_location():
    def get_location(name):
        reach_api("location", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_location)
    atheris.Fuzz()


def test_location_area():
    def get_location_area(name):
        reach_api("location-area", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_location_area)
    atheris.Fuzz()


def test_machine():
    def get_machine(name):
        reach_api("machine", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_machine)
    atheris.Fuzz()


def test_move():
    def get_move(name):
        reach_api("move", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_move)
    atheris.Fuzz()


def test_move_ailment():
    def get_move_ailment(name):
        reach_api("move-ailment", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_move_ailment)
    atheris.Fuzz()


def test_move_battle_style():
    def get_move_battle_style(name):
        reach_api("move-battle-style", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_move_battle_style)
    atheris.Fuzz()


def test_move_category():
    def get_move_category(name):
        reach_api("move-category", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_move_category)
    atheris.Fuzz()


def test_move_damage_class():
    def get_move_damage_class(name):
        reach_api("move-damage-class", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_move_damage_class)
    atheris.Fuzz()


def test_move_learn_method():
    def get_move_learn_method(name):
        reach_api("move-learn-method", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_move_learn_method)
    atheris.Fuzz()


def test_move_target():
    def get_move_target(name):
        reach_api("move-target", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_move_target)
    atheris.Fuzz()


def test_nature():
    def get_nature(name):
        reach_api("nature", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_nature)
    atheris.Fuzz()


def test_pal_park_area():
    def get_pal_park_area(name):
        reach_api("pal-park-area", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_pal_park_area)
    atheris.Fuzz()


def test_pokedex():
    def get_pokedex(name):
        reach_api("pokedex", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_pokedex)
    atheris.Fuzz()


def test_pokemon():
    def get_pokemon(name):
        reach_api("pokemon", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_pokemon)
    atheris.Fuzz()


def test_pokemon_color():
    def get_pokemon_color(name):
        reach_api("pokemon-color", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_pokemon_color)
    atheris.Fuzz()


def test_pokemon_form():
    def get_pokemon_form(name):
        reach_api("pokemon-form", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_pokemon_form)
    atheris.Fuzz()


def test_pokemon_habitat():
    def get_pokemon_habitat(name):
        reach_api("pokemon-habitat", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_pokemon_habitat)
    atheris.Fuzz()


def test_pokemon_shape():
    def get_pokemon_shape(name):
        reach_api("pokemon-shape", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_pokemon_shape)
    atheris.Fuzz()


def test_pokemon_species():
    def get_pokemon_species(name):
        reach_api("pokemon-species", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_pokemon_species)
    atheris.Fuzz()


def test_pokeathlon_stat():
    def get_pokeathlon_stat(name):
        reach_api("pokeathlon-stat", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_pokeathlon_stat)
    atheris.Fuzz()


def test_region():
    def get_region(name):
        reach_api("region", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_region)
    atheris.Fuzz()


def test_stat():
    def get_stat(name):
        reach_api("stat", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_stat)
    atheris.Fuzz()


def test_super_contest_effect():
    def get_super_contest_effect(name):
        reach_api("super-contest-effect", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_super_contest_effect)
    atheris.Fuzz()


def test_type():
    def get_type(name):
        reach_api("type", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_type)
    atheris.Fuzz()


def test_version():
    def get_version(name):
        reach_api("version", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_version)
    atheris.Fuzz()


def test_version_group():
    def get_version_group(name):
        reach_api("version-group", {"name": str(name)})

    atheris.Setup([sys.argv[0], "-runs=100"], get_version_group)
    atheris.Fuzz()
