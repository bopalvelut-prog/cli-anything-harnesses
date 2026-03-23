import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rebar3 running')
@cli.command()
def start(): click.echo('rebar3 started')
if __name__ == '__main__': cli()
