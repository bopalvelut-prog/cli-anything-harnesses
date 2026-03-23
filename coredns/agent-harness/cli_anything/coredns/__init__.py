import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('coredns running')
@cli.command()
def start(): click.echo('coredns started')
if __name__ == '__main__': cli()
