import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('aws_sqs_v4 running')
@cli.command()
def start(): click.echo('aws_sqs_v4 started')
if __name__ == '__main__': cli()
