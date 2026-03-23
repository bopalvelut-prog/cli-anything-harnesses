import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('aws_config running')
@cli.command()
def start(): click.echo('aws_config started')
if __name__ == '__main__': cli()
