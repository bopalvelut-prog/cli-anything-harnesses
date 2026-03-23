import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('regular running')
@cli.command()
def start(): click.echo('regular started')
if __name__ == '__main__': cli()
