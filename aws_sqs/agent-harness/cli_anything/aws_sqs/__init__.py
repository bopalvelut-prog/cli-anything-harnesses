import click
@click.group()
def cli(): pass
@cli.command()
def queues(): click.echo('SQS queues')
@cli.command()
def send(): click.echo('SQS send')
if __name__ == '__main__': cli()
