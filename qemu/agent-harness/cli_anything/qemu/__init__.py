import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('qemu running')
@cli.command()
def start(): click.echo('qemu started')
if __name__ == '__main__': cli()
