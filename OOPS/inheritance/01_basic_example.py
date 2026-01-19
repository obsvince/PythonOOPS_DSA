class Virus:
    pass


class RNAVirus(Virus):
    pass


class CoronaVirus(RNAVirus):
    pass


class SARSCov2(CoronaVirus):
    pass


if __name__ == '__main__':
    # All are true because they are inherited as a hierarchy.
    # SARSCov2 is a CoronaVirus is a RNAVirus is a Virus
    print(issubclass(SARSCov2, CoronaVirus))
    print(issubclass(CoronaVirus, RNAVirus))
    print(issubclass(SARSCov2, Virus))

    # True because Virus inherits from object class.
    print(issubclass(Virus, object))
    print(issubclass(object, Virus)) # the reverse is False.
