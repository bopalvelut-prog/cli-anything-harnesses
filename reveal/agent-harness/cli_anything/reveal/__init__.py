import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('reveal running')
@cli.command()
def start(): click.echo('reveal started')
if __name__ == '__main__': cli()
