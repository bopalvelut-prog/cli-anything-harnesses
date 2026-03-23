import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('libyaml running')
@cli.command()
def start(): click.echo('libyaml started')
if __name__ == '__main__': cli()
