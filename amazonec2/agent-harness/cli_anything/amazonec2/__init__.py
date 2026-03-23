import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('amazonec2 running')
@cli.command()
def start(): click.echo('amazonec2 started')
if __name__ == '__main__': cli()
