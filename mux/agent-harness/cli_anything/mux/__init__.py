import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mux running')
@cli.command()
def start(): click.echo('mux started')
if __name__ == '__main__': cli()
