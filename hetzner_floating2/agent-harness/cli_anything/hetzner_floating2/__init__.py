import click
@click.group()
def cli(): pass
@cli.command()
def list(): click.echo('Floating IPs v2')
if __name__ == '__main__': cli()
