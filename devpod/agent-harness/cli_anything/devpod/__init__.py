import click
@click.group()
def cli(): pass
@cli.command()
def up(): click.echo('DevPod up')
@cli.command()
def status(): click.echo('DevPod status')
if __name__ == '__main__': cli()
