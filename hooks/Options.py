# Object classes from AP that represent different types of options that you can create
from Options import Option, FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange, OptionGroup, PerGameCommonOptions, OptionSet
# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value
from typing import Type, Any


####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#
class TotalModules(Range):
    """Total Number of modules to randomly generate."""
    range_start = 1
    range_end = 2000
    default = 50

class StartingModules(Range):
    """Number of modules to randomly add to the starting inventory."""
    range_start = 1
    range_end = 20
    default = 5

class CompletionPercentage(Range):
    """Percent of modules which must be completed in order to goal."""
    range_start = 10
    range_end = 100
    default = 75

class ModuleVetos(OptionSet):
    """Prevents listed modules from appearing.
    Type "_extremes" to include all extreme rated modules."""

class ModuleForces(OptionSet):
    """Forces listed modules to appear."""

class Seed(Range):
    """Seed used to generate which modules are chosen.
    Recommended to keep it at random."""
    display_name = "generator_seed"
    range_start = 0
    range_end = 10000000
    default = "random"

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict[str, Type[Option[Any]]]) -> dict[str, Type[Option[Any]]]:
    options["total_modules"] = TotalModules
    options["starting_modules"] = StartingModules
    options["completion_percentage"] = CompletionPercentage
    options["module_vetos"] = ModuleVetos
    options["module_forces"] = ModuleForces
    options["_seed"] = Seed
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: Type[PerGameCommonOptions]):
    # To access a modifiable version of options check the dict in options.type_hints
    # For example if you want to change DLC_enabled's display name you would do:
    # options.type_hints["DLC_enabled"].display_name = "New Display Name"

    #  Here's an example on how to add your aliases to the generated goal
    # options.type_hints['goal'].aliases.update({"example": 0, "second_alias": 1})
    # options.type_hints['goal'].options.update({"example": 0, "second_alias": 1})  #for an alias to be valid it must also be in options

    pass

# Use this Hook if you want to add your Option to an Option group (existing or not)
def before_option_groups_created(groups: dict[str, list[Type[Option[Any]]]]) -> dict[str, list[Type[Option[Any]]]]:
    # Uses the format groups['GroupName'] = [TotalCharactersToWinWith]
    return groups

def after_option_groups_created(groups: list[OptionGroup]) -> list[OptionGroup]:
    return groups
