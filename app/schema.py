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



class CreateCandidate(graphene.Mutation):
    class Arguments:
        name = graphene.String()
    ok = graphene.Boolean()
    post = graphene.Field(lambda:CandidateObject)
    def mutate(self, info, name):
        new_candidate = CandidateModel(name=name)
        db.session.add(new_candidate)
        db.session.commit()
        ok =True
        return CreateCandidate(candidate = new_candidate,ok=ok)

class PostObject(SQLAlchemyObjectType):
   class Meta:
       model = PostModel
       interfaces = (graphene.relay.Node, ) 


class CreatePost(graphene.Mutation):
    class Arguments:
        name = graphene.String()
    ok = graphene.Boolean()
    post = graphene.Field(lambda:PostObject)
    def mutate(self, info, name):
        new_post = PostModel(name=name)
        db.session.add(new_post)
        db.session.commit()
        ok =True
        return CreatePost(post = new_post,ok=ok)


class DistrictObject(SQLAlchemyObjectType):
    class Meta:
       model = DistrictModel
       interfaces = (graphene.relay.Node, )


class DistrictConnection(graphene.Connection):
    class Meta:
        node = DistrictObject
    count = graphene.Int()

    def resolve_count(root, info):
        return len(root.edges)

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
       interfaces = (relay.Node,) 

class CreateCounty(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    ok = graphene.Boolean()
    county =graphene.Field(lambda:CountyObject)

    def mutate(self, info, name):
        new_county = CountyModel(name=name)


        db.session.add(new_county)
        db.session.commit()
        ok =True
        return CreateCounty(county = new_county,ok=ok)


class SubCountyObject(SQLAlchemyObjectType):
   class Meta:
       model = SubCountyModel
       interfaces = (relay.Node,) 


class CreateSubCounty(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    ok = graphene.Boolean()
    subcounty =graphene.Field(lambda:SubCountyObject)

    def mutate(self, info, name):
        new_subcounty = SubCountyModel(name=name)


        db.session.add(new_subcounty)
        db.session.commit()
        ok =True
        return CreateSubCounty(subcounty = new_subcounty,ok=ok)



       
class ParishObject(SQLAlchemyObjectType):
   class Meta:
       model = ParishModel

       interfaces = (relay.Node,) 


class CreateParish(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    ok = graphene.Boolean()
    parish =graphene.Field(lambda:ParishObject)

    def mutate(self, info, name):
        new_parish = ParishModel(name=name)


        db.session.add(new_parish)
        db.session.commit()
        ok =True
        return CreateParish(parish = new_parish,ok=ok)

      
class VillageObject(SQLAlchemyObjectType):
   class Meta:
       model = VillageModel
       interfaces = (relay.Node,) 

class CreateVillage(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    ok = graphene.Boolean()
    village =graphene.Field(lambda:VillageObject)

    def mutate(self, info, name):
        new_village = VillageModel(name=name)


        db.session.add(new_village)
        db.session.commit()
        ok =True
        return CreateVillage(village = new_village,ok=ok)

      
class PartyObject(SQLAlchemyObjectType):
   class Meta:
       model = PartyModel
       interfaces = (relay.Node,) 


class CreateParty(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    ok = graphene.Boolean()
    party =graphene.Field(lambda:PartyObject)

    def mutate(self, info, name):
        new_party = PartyModel(name=name)


        db.session.add(new_party)
        db.session.commit()
        ok =True
        return CreateParty(party = new_party,ok=ok)



class Mutation(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    create_district = CreateDistrict.Field()
    create_county = CreateCounty.Field()
    create_subcounty = CreateCounty.Field()
    create_candidate = CreateCandidate.Field()
    create_parish = CreateParish.Field()
class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    candidates = graphene.ConnectionField(CandidateObject.connection)
    # districts = graphene.List(DistrictObject,first=graphene.Int(),last=graphene.Int())
    posts = graphene.ConnectionField(PostObject.connection)
    parties = graphene.ConnectionField(PartyObject.connection)
    counties = graphene.ConnectionField(CountyObject.connection)
    subcounties = graphene.ConnectionField(SubCountyObject.connection)
    villages = graphene.ConnectionField(VillageObject.connection)
    parishes =  graphene.ConnectionField(ParishObject.connection)
    district = graphene.relay.Node.Field(DistrictObject.connection)
    districts = graphene.ConnectionField(DistrictObject.connection)
    
    def paginator(query):
        pass
        
       
    def resolve_candidates(self,info,**kwargs):
        query = CandidateObject.get_query(info)
        return query.all()


    def resolve_districts(self,info,**kwargs):
        query = DistrictObject.get_query(info)
        return query.all()
    def resolve_counties(self,info,**kwargs):
        query = CountyObject.get_query(info)
        return query.all()
    


    def resolve_subcounties(self,info,**kwargs):
        query = SubCountyObject.get_query(info)
        return query.all()

    def resolve_villages(self,info):
        query = VillageObject.get_query(info)
        return query.all()

    def resolve_posts(self,info):
        query = PostObject.get_query(info)
        return query.all()

    def resolve_parties(self,info):
        query = PartyObject.get_query(info)
        return query.all()


    def resolve_parishes(self,info):
        query = ParishObject.get_query(info)
        return query.all()





schema =graphene.Schema(query=Query,mutation = Mutation)
