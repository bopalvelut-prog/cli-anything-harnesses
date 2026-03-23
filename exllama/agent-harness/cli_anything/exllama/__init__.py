import click
@click.group()
def cli(): pass
@cli.command()
def run(): click.echo('ExLlama run')
@cli.command()
def benchmark(): click.echo('ExLlama benchmark')
if __name__ == '__main__': cli()
