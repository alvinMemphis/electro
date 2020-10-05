import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import Party as PartyModel,District as DistrictModel,Posts as PostModel,County as CountyModel,SubCounty as SubCountyModel, Village as VillageModel,Candidates as CandidateModel,Parish as ParishModel

from graphql import GraphQLSchema







# Schema Objects



class CandidateObject(SQLAlchemyObjectType):
   class Meta:
       model = CandidateModel


class PostObject(SQLAlchemyObjectType):
   class Meta:
       model = PostModel


class DistrictObject(SQLAlchemyObjectType):
   class Meta:
       model = DistrictModel



class CountyObject(SQLAlchemyObjectType):
   class Meta:
       model = CountyModel

class SubCountyObject(SQLAlchemyObjectType):
   class Meta:
       model = SubCountyModel

class ParisheObject(SQLAlchemyObjectType):
   class Meta:
       model = ParishModel
class VillageObject(SQLAlchemyObjectType):
   class Meta:
       model = VillageModel
class PartyObject(SQLAlchemyObjectType):
   class Meta:
       model = PartyModel





class Query(graphene.ObjectType):
    candidaites = graphene.List(CandidateObject)
    def candidate_resolver(self,info):
        query = CandidateObject.get_query(info)
        return query.all()





schema =graphene.Schema(query=Query)
