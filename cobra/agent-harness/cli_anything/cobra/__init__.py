import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cobra running')
@cli.command()
def start(): click.echo('cobra started')
if __name__ == '__main__': cli()
