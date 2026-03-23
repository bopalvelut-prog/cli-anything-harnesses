import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('hop running')
@cli.command()
def start(): click.echo('hop started')
if __name__ == '__main__': cli()
