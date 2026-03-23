import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('aws_timestream running')
@cli.command()
def start(): click.echo('aws_timestream started')
if __name__ == '__main__': cli()
