from sqlalchemy import Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


fields = {
    'id': '唯一标识符',
    'chinese_name': '中文名称',
    'latin_name': '拉丁名称',
    'tibetan_name': '藏文名称及音译名',
    'tibetan_medical_effectiveness': '藏医应用',
    'chinese_medical_preparation': '中医炮制方法',
    'tibetan_medical_preparation': '藏医炮制方法',
    'create_time': '条目创建时间',
    'update_time': '条目更新时间',
    'medicinal_part': '药用部位',
    'geometrical_information': '分布地区',
    'properties': '性味归经',
    'indicative_diseases': '功效主治',
    'medicine_composition': '方剂',
    'medicine_name': '药材名称',
    'alias': '别名',
    'usage_methods': '用法用量',
    'pharmacology': '药理作用',
    'clinical_manifest': '临床应用',
    'main_chemical': '主要活性成分',
    'plant_morphological_feature': '植物形态',
    'images': '相关图片'
}


class Base(DeclarativeBase):
    pass


class Medicine(Base):
    __tablename__ = 'medicine_table'
    id: Mapped[int] = mapped_column(primary_key=True)
    chinese_name: Mapped[str] = mapped_column(Text)
    latin_name: Mapped[str] = mapped_column(Text)
    tibetan_name: Mapped[str] = mapped_column(Text)
    tibetan_medical_effectiveness: Mapped[str] = mapped_column(Text)
    chinese_medical_preparation: Mapped[str] = mapped_column(Text)
    tibetan_medical_preparation: Mapped[str] = mapped_column(Text)
    create_time: Mapped[str] = mapped_column(Text)
    update_time: Mapped[str] = mapped_column(Text)
    medicinal_part: Mapped[str] = mapped_column(Text)
    geometrical_information: Mapped[str] = mapped_column(Text)
    properties: Mapped[str] = mapped_column(Text)
    indicative_diseases: Mapped[str] = mapped_column(Text)
    medicine_composition: Mapped[str] = mapped_column(Text)
    medicine_name: Mapped[str] = mapped_column(Text)
    alias: Mapped[str] = mapped_column(Text)
    usage_methods: Mapped[str] = mapped_column(Text)
    pharmacology: Mapped[str] = mapped_column(Text)
    clinical_manifest: Mapped[str] = mapped_column(Text)
    main_chemical: Mapped[str] = mapped_column(Text)
    plant_morphological_feature: Mapped[str] = mapped_column(Text)
