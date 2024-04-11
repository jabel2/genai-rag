import streamlit as st
from langchain_community.graphs import Neo4jGraph

graph = Neo4jGraph(
    url="bolt://neo4j:7687",
    username="neo4j",
    password="neo4juser"
)