import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('rule')
@click.argument('target')
def scan(rule, target): subprocess.run(['yara', rule, target])
if __name__ == '__main__': cli()
