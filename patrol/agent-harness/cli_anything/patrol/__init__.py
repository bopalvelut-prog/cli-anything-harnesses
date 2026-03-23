import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('patrol running')
@cli.command()
def start(): click.echo('patrol started')
if __name__ == '__main__': cli()
