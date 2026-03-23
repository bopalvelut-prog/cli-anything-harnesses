import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('virtualbox_v3 running')
@cli.command()
def start(): click.echo('virtualbox_v3 started')
if __name__ == '__main__': cli()
