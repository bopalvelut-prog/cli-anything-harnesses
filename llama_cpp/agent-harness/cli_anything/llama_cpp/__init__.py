import click
@click.group()
def cli(): pass
@cli.command()
def run(): click.echo('llama.cpp run')
@cli.command()
def quantize(): click.echo('llama.cpp quantize')
if __name__ == '__main__': cli()
