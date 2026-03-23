import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('aws_eventbridge running')
@cli.command()
def start(): click.echo('aws_eventbridge started')
if __name__ == '__main__': cli()
