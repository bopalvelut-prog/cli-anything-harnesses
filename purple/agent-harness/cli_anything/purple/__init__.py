import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('purple running')
@cli.command()
def start(): click.echo('purple started')
if __name__ == '__main__': cli()
