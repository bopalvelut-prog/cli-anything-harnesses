import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('aiven running')
@cli.command()
def start(): click.echo('aiven started')
if __name__ == '__main__': cli()
