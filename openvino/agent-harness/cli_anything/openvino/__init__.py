import click
@click.group()
def cli(): pass
@cli.command()
def convert(): click.echo('OpenVINO convert')
@cli.command()
def benchmark(): click.echo('OpenVINO benchmark')
if __name__ == '__main__': cli()
