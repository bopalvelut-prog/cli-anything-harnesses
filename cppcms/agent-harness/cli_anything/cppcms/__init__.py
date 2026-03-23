import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cppcms running')
@cli.command()
def start(): click.echo('cppcms started')
if __name__ == '__main__': cli()
