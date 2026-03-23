import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('civil running')
@cli.command()
def start(): click.echo('civil started')
if __name__ == '__main__': cli()
