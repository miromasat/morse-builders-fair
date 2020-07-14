#!/usr/bin/env python3

from aws_cdk import core

from morse_builders_fair.morse_builders_fair_stack import MorseBuildersFairStack


app = core.App()
MorseBuildersFairStack(app, "morse-builders-fair", env={'region': 'us-west-2'})

app.synth()
