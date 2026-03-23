import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('archlinux running')
@cli.command()
def start(): click.echo('archlinux started')
if __name__ == '__main__': cli()
