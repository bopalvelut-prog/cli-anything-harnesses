import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('unicorn running')
@cli.command()
def start(): click.echo('unicorn started')
if __name__ == '__main__': cli()
