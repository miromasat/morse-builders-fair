from aws_cdk import (
    aws_iam as iam,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
    aws_s3 as s3, 
    core
)


class MorseBuildersFairStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        queue = sqs.Queue(
            self, "MorseBuildersFairQueue",
            visibility_timeout=core.Duration.seconds(300),
        )

        topic = sns.Topic(
            self, "MorseBuildersFairTopic"
        )

        topic.add_subscription(subs.SqsSubscription(queue))
