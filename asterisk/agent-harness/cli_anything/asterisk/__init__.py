import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('asterisk running')
@cli.command()
def start(): click.echo('asterisk started')
if __name__ == '__main__': cli()
