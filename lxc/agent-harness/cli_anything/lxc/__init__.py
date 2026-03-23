import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('lxc running')
@cli.command()
def start(): click.echo('lxc started')
if __name__ == '__main__': cli()
