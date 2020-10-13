import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from .models import Party as PartyModel,District as DistrictModel,Posts as PostModel,County as CountyModel,SubCounty as SubCountyModel, Village as VillageModel,Candidates as CandidateModel,Parish as ParishModel
from app import db
from graphql import GraphQLSchema


class CandidateObject(SQLAlchemyObjectType):
   class Meta:
       model = CandidateModel
       interfaces = (graphene.relay.Node, )


class PostObject(SQLAlchemyObjectType):
   class Meta:
       model = PostModel
       interfaces = (graphene.relay.Node, ) 

class DistrictObject(SQLAlchemyObjectType):
   class Meta:
       model = DistrictModel
       interfaces = (graphene.relay.Node, )
class CreateDistrict(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    ok = graphene.Boolean()
    district =graphene.Field(lambda:DistrictObject)

    def mutate(self, info, name):
        new_district = DistrictModel(name=name)


        db.session.add(new_district)
        db.session.commit()
        ok =True
        return CreateDistrict(district = new_district,ok=ok)


class CountyObject(SQLAlchemyObjectType):
   class Meta:
       model = CountyModel

class SubCountyObject(SQLAlchemyObjectType):
   class Meta:
       model = SubCountyModel
       interfaces = (relay.Node,) 
class ParisheObject(SQLAlchemyObjectType):
   class Meta:
       model = ParishModel

       interfaces = (relay.Node,) 
class VillageObject(SQLAlchemyObjectType):
   class Meta:
       model = VillageModel
       interfaces = (relay.Node,) 
class PartyObject(SQLAlchemyObjectType):
   class Meta:
       model = PartyModel
       interfaces = (relay.Node,) 


class Mutation(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    create_district = CreateDistrict.Field()

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    candidates = SQLAlchemyConnectionField(CandidateObject)
    all_districts =  SQLAlchemyConnectionField(DistrictObject)
    def candidate_resolver(self,info):
        query = CandidateObject.get_query(info)
        return query.all()
    def district_resolver(self,info):
        query = DistrictObject.get_query(info)
        return query.all()



schema =graphene.Schema(query=Query,mutation = Mutation)
