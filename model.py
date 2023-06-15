1장

2장
class문으로 sample과 하위클래스인 knownsample 클래스 정의 작성

class Sample:
    pass

class KnownSample(Sample):
    def __init__(
        self,
        sepal_length: float,
        sepal_width: float,
        petal_length: float,
        petal_width: float,
        purpose: int,
        species: str,
    ) -> None:
        purpose_enum = Purpose(purpose)
        if purpose_enum not in {Purpose.Training, Purpose.Testing}:
            raise ValueError(f"Invalid purpose: {purpose!r}: {purpose_enum}")
        super().__init__(
            sepal_length=sepal_length,
            sepal_width=sepal_width,
            petal_length=petal_length,
            petal_width=petal_width,
        )
        self.species = species
    def __repr__(self) -> str:
        return(
            f"{self.__class__.__name}("
            f"sepal_length={self.sepal_length}, "
            f"sepal_width={self.sepal_width}, "
            f"petal_length={self.petal_length}, "
            f"petal_width={self.petal_width}, "
            f"species={self.species!r}, "
            f")"
        )    

class Distance:
    """거리 계산에 대한 정의"""
    def distance(self,s1:Sample, s2:Sample)->float:
        pass

class ValueError:
    pass

class InvalidSampleError(ValueError):
    """소스 데이터 파일이 유효하지 않은 데이터 표현을 가지고 있다."""        

class OutlierError(ValueError):
    """값이 예상된 범위 밖에 있다"""    

sepal_length
sepal_width
petal_length
petal_width      