import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('matriux running')
@cli.command()
def start(): click.echo('matriux started')
if __name__ == '__main__': cli()
