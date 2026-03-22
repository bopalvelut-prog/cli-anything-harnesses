import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('file')
def run(file): subprocess.run(['deno', 'run', '--allow-all', file])
@cli.command()
def check(): subprocess.run(['deno', 'check', 'main.ts'])
if __name__ == '__main__': cli()
