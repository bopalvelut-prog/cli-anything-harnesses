import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('elixir running')
@cli.command()
def start(): click.echo('elixir started')
if __name__ == '__main__': cli()
