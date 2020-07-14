import json
import pytest

from aws_cdk import core
from morse-builders-fair.morse_builders_fair_stack import MorseBuildersFairStack


def get_template():
    app = core.App()
    MorseBuildersFairStack(app, "morse-builders-fair")
    return json.dumps(app.synth().get_stack("morse-builders-fair").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
