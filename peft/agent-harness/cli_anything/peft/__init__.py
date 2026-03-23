import click
@click.group()
def cli(): pass
@cli.command()
def train(): click.echo('PEFT train')
@cli.command()
def merge(): click.echo('PEFT merge')
if __name__ == '__main__': cli()
