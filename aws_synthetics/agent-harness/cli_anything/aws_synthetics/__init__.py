import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('aws_synthetics running')
@cli.command()
def start(): click.echo('aws_synthetics started')
if __name__ == '__main__': cli()
